schema = {
    "type": "object",
    
    "patternProperties": {
        "^[a-zA-Z_][a-zA-Z0-9_]*$": {"type": "string", "pattern": "^[a-zA-Z_][a-zA-Z0-9_]*$"}
    },
    
    "additionalProperties": False
}