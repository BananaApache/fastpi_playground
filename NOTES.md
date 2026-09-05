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

### Basic Core Concepts

Needed for most projects

1. Path operations — @app.get("/ipos"), path params, query params with defaults.
2. Pydantic models in and out — request bodies validate automatically, and response_model= shapes what goes out.
3. Depends() — dependency injection. This is the FastAPI concept. You'll use it for your DB connection and later for auth.
4. async def vs def — if the function calls blocking code, make it def and FastAPI threadpools it.
5. APIRouter — splits routes across files.
6. lifespan — where you open and close your asyncpg pool. Startup/shutdown hooks.
7. HTTPException — error responses. Plus a global handler eventually.
8. CORSMiddleware - self explanatory



