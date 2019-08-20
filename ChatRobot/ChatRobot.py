
import NLU_core
import Data_Collector
import json

message = "I'm looking for a chinese food"

result = NLU_core.interpreter.parse(message)
print(json.dumps(result,indent=2))

message = "show me chinese restaurants"
result = NLU_core.interpreter.parse(message)
print(json.dumps(result,indent=2))