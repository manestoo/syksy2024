import asyncio
import mysql.connector
from bleak import BleakClient

# Nordic BLE device address and characteristic UUID
DEVICE_ADDRESS = "D7:E2:86:DD:5D:99"
CHARACTERISTIC_UUID = "00001526-1212-efde-1523-785feabcd123"

# MySQL database connection configuration
db_config = {
    'user': 'dbaccess_rw',
    'password': 'fasdjkf2389vw2c3k234vk2f3',
    'host': '172.20.241.9',
    'database': 'measurements'  # Your database name
}

# Global list to store received data packets and a flag for processing state
received_data = []
is_processing = False

# Data handler function to parse data and insert into MySQL
def data_handler(sender, data):
    global received_data, is_processing

    # If data is already being processed, return early to prevent duplication
    if is_processing:
        return

    # Print the raw data for debugging
    print("Raw data received:", data.hex())

    # Store the received data packet
    received_data.append(data)

    # If we have received 4 data packets, process and insert into database
    if len(received_data) == 4:
        # Set the processing flag to True to avoid processing more data until done
        is_processing = True

        # Ensure data alignment - x, y, z, suunta
        sensor_x = int.from_bytes(received_data[0], 'little') / 100.0
        sensor_y = int.from_bytes(received_data[1], 'little') / 100.0
        sensor_z = int.from_bytes(received_data[2], 'little') / 100.0
        suunta = int.from_bytes(received_data[3], 'little')

        # Connect to MySQL database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Insert parsed data into the `rawdata` table
        insert_query = """
        INSERT INTO rawdata (groupid, from_mac, to_mac, sensorvalue_a, sensorvalue_b, sensorvalue_c, 
                             sensorvalue_d, sensorvalue_e, sensorvalue_f)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # Example values (replace as needed)
        groupid = 22  # Replace with actual group ID
        from_mac = "0"
        to_mac = "0"  # Set or retrieve actual `to_mac`

        cursor.execute(insert_query, (groupid, from_mac, to_mac, sensor_x, sensor_y, 
                                      sensor_z, suunta, 0, ""))  # Placeholder for other columns

        # Commit the transaction
        conn.commit()
        print("Data inserted into database:", sensor_x, sensor_y, sensor_z, suunta)

        # Clear the received_data list to wait for the next 4 packets
        received_data = []

        # Reset processing flag to allow next data batch
        is_processing = False

        # Close the cursor and connection
        cursor.close()
        conn.close()

# Main function to handle BLE connection and data notification
async def main():
    # Create BLE client for Nordic device
    async with BleakClient(DEVICE_ADDRESS) as client:
        # Check if device is connected
        if client.is_connected:
            print("Connected to device!")
            
            # Start receiving notifications
            await client.start_notify(CHARACTERISTIC_UUID, data_handler)
            print("Waiting for data...")

            # Wait for 30 seconds or any desired period
            await asyncio.sleep(30)

            # Stop notifications and disconnect
            await client.stop_notify(CHARACTERISTIC_UUID)
            print("Disconnected from device")

# Run the main function
asyncio.run(main())
