import os
import json
import httpx
from dotenv import load_dotenv


async def get_imei(device_id):
    url = "https://api.imeicheck.net/v1/checks"
    headers = {
        "Authorization": "Bearer " + os.environ.get("TOEKN_API_LIVE"),
        "Content-Type": "application/json",
    }

    body = json.dumps({"deviceId": str(device_id), "serviceId": 1})

    async with httpx.AsyncClient() as client:
        text_imei = await client.post(url, headers=headers, data=body)
        return text_imei.text


if __name__ == "__main__":
    load_dotenv()
    print(get_imei("123456789012345"))
