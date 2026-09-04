# NOTES

### Quickstart

1. After importing FastAPI create instance
2. Define path operations:
```
@app.get("/")
async def root():
    return {"message": "Hello World"}

```
- List of operators:
```
@app.post()
@app.put()
@app.delete()
@app.options()
@app.head()
@app.patch()
@app.trace()
```

