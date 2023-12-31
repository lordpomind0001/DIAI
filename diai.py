import aiohttp
async def request(message, apikey, func):
    request_headers = {'Authorization': apikey}
    async with aiohttp.ClientSession() as session:                                     
        api_url = 'http://us3.techstar.live:55565/request'
        request_data = {'message': user_message,'message-author-id': message.author.id,'message-author-user': message.author.name,'function': func}
        async with session.post(api_url, json=request_data, headers=request_headers) as response:
            api_response = await response.json()
            return api_response, response
