# python_scripts/chart_electricity_prices.py
# Fetching data from the Nordpool energy prices sensor and formatting it for charting

# Define chart data structure
chart_data = {
    'labels': [],
    'prices': []
}

# Fetch the sensor data
sensor_data = hass.states.get('sensor.nordpool_kwh_be_eur_3_10_021')
logger.debug("Raw energy Prices:",sensor_data) 

# Debug: log the raw sensor data
if sensor_data is not None:
    logger.info("Raw energy Data: {}".format(sensor_data.attributes))  # Log the attributes of the sensor

    # Access the raw_today attribute
    raw_today = sensor_data.attributes.get('raw_today', [])
    logger.info("Raw Today Prices: {}".format(raw_today))  # Log the raw_today data

    # Populate the chart_data
    for entry in raw_today:
        start_time = entry['start']  # Extracting the start time
        price_value = entry['value']  # Extracting the price value

        # Append to chart data
        chart_data['labels'].append(start_time)
        chart_data['prices'].append(price_value)

    # Log the final chart_data for debugging
    logger.info("Chart Data: {}".format(chart_data))
    
    # Return data through output
    output = {}
    output['labels'] = chart_data['labels']
    output['prices'] = chart_data['prices']
else:
    logger.error("Sensor data not found for 'sensor.nordpool_kwh_be_eur_3_10_021'")
    output = {}
    output['error'] = "Sensor data not found"
