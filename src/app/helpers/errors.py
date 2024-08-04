from fastapi.responses import JSONResponse

def format_error_response(error: Exception, status_code: int = 500) -> JSONResponse:
  content = {
    'error': error.__class__.__name__,
    'message': str(error)
  }

  return JSONResponse(content=content, status_code=status_code)