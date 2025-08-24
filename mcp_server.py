from mcp.server.fastmcp import FastMCP
from pydantic import Field
from contents import docs

mcp = FastMCP("DocumentMCP", log_level="ERROR")

docs = docs

# A tool to read a document
@mcp.tool(
    name="read_doc_contents",
    description="Read the contenets of the document and return it as a string."    
)
def read_document(
    doc_id: str = Field(description="Id of the document to read")
):
    if doc_id not in docs:
        raise ValueError(f"Doc with {doc_id} is not found")
    return docs[doc_id]


# A tool to edit a document
@mcp.tool(
    name="edit_document",
    description="Edit a document by replacing a string in the docuemnt content with a new string"
)
def edit_document(
    doc_id: str = Field(description="Id of the docuement that will be edited."),
    old_str: str = Field(description="The text to replace. Must Match exactly including white space"),
    new_str: str = Field(description="The new text to insert in place of the old text.")
):
    if doc_id not in docs:
        raise ValueError(f"Doc with {doc_id} is not found")
    docs[doc_id] = docs[doc_id].replace(old_str, new_str)