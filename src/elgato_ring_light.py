from ebbs import Builder
import requests
import logging

class elgato_ring_light(Builder):
	def __init__(this, name="Elgato Ring Light"):
		super().__init__(name)

		this.requiredKWArgs.append("elgato_ring_light_ip")

		this.optionalKWArgs['brightness'] = 50
		this.optionalKWArgs['temperature'] = 4000
		this.optionalKWArgs['on'] = True

	def Build(this):
		requestData = {
			"lights": [
				{
					"on": int(this.on),
					"brightness": this.brightness,
					"temperature": this.temperature
				}
			]
		}

		r = requests.put(f"http://{this.elgato_ring_light_ip}:9123/elgato/lights", json=requestData)
		logging.debug(f"Sent: {r.request.body} with headers: {r.request.headers}")
		logging.debug(f"Elgato Ring Light Response ({r.status_code}): {r.text}")