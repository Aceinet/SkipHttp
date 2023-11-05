"""
SkipHttp
-------------------
Just a small library to properly get/post data from url, originally meant to be a geometry dash servers scraper

Made by Aceinet
"""


import asyncio, aiohttp

ACCEPT_ENCODING = "Accept-Encoding"
USER_AGENT = "User-Agent"
SKIP_HEADERS = (ACCEPT_ENCODING, USER_AGENT)


class Response:
  """Response

  Http result given from request_post, request_get

  Containing:
      text (str): Result text from request
      headers (dict): Request headers
      status (int): Http status
  """
  def __init__(self, text: str, headers: dict, status: int) -> None:
    self.text = text
    self.headers = headers
    self.status = status
  
  def __repr__(self) -> str:
    return "<Response [%d]>" % self.status

def request_post(url: str, params: dict, **kwargs) -> Response:
  """POST request method

  Args:
      url (str): Request url
      params (dict): Parameters to POST method

  Returns:
      Response: Http response containing text, headers, status
  """
  if "skip_auto_headers" not in kwargs:
    kwargs['skip_auto_headers'] = SKIP_HEADERS
    
  async def async_request(url, params, **kwargs):
    async with aiohttp.ClientSession(**kwargs) as session: 
      async with session.post(url, data=params) as response: 
        txt = await response.text()
        status = response.status
        headers = response.headers
        return Response(txt, headers, status)

  return asyncio.run(async_request(url, params, **kwargs))

def request_get(url: str, **kwargs) -> Response:
  """GET request method

  Args:
      url (str): Request url

  Returns:
      Response: Http response containing text, headers, status
  """
  if "skip_auto_headers" not in kwargs:
    kwargs['skip_auto_headers'] = SKIP_HEADERS
    
  async def async_request(url, **kwargs):
    async with aiohttp.ClientSession(**kwargs) as session: 
      async with session.get(url) as response: 
        txt = await response.text()
        status = response.status
        headers = response.headers
        return Response(txt, headers, status)

  return asyncio.run(async_request(url, **kwargs))