# python_scripts/chart_electricity_prices.py
# Fetching data from the Nordpool energy prices sensor and formatting it for charting

# Parameters passed to the script
# logger.error("=====>Script started")
sensor_entity = data.get('sensor_entity')
prices_property = data.get('prices_property')

# Define chart data structure
chart_data = {
    'labels': [],
    'prices': []
}

# Fetch the sensor data
sensor_data = hass.states.get(sensor_entity)

# Debug: log the raw sensor data
if sensor_data is not None:
    # logger.error("=====>Raw energy Data: {}".format(sensor_data.attributes))  # Log the attributes of the sensor

    # Access the specified raw property
    raw_data = sensor_data.attributes.get(prices_property, [])
    # logger.error("=====>Raw Data for {}: {}".format(prices_property, raw_data))  # Log the specified raw data

    # Populate the chart data
    for entry in raw_data:
        start_time = entry['start']  # Extracting the start time
        price_value = entry['value']  # Extracting the price value

        # Append to chart data
        chart_data['labels'].append(start_time)
        chart_data['prices'].append(price_value)

    # Log the final chart_data for debugging
    # logger.error("=====>Chart Data: {}".format(chart_data))
        
    # Return data through output
    output = {}
    output['labels'] = chart_data['labels']
    output['prices'] = chart_data['prices']

else:
    error_message = "=====>Sensor data not found for '{}'".format(sensor_entity)
    output = {}
    output['error'] = error_message