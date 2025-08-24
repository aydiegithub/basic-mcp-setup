from fastmcp import FastMCP
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware

load_dotenv()

mcp = FastMCP(name="Notes App")

@mcp.tool(
    name="Get My Notes",
    description="This is used to get the notes."
)
def get_my_notes() -> str:
    """ 
    Get all notes for a user
    """
    return "no notes"

@mcp.tool(
    name="Add Notes",
    description="This is used to add notes."
)
def add_note(content: str) -> str:
    """ 
    Add a note for a user
    """
    return f"added note: {content}"

if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="127.0.0.1",
        port=8000,
        middleware=[
            Middleware(
                CORSMiddleware,
                allow_origins=['*'],
                allow_credentials=True,
                allow_methods=['*'],
                allow_headers=['*'],
            )
        ]
    )