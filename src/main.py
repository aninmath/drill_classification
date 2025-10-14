from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Literal, Optional
from langchain_core.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash', api_key= 'AIzaSyCS36bFxt4Y08dqom9MqrsGNEStZ6MmIPM')


class Drill(BaseModel):
    drill_or_not : Literal['Drill', 'Not Drill'] = Field(description= "mention whether its a valid drill or not, if not a drill mention 'not drill")
    drill_type : Literal[
    "Fire/Explosion",
    "Rescue",
    "LOPC",
    "Medical",
    "Security Event",
    "Natural Disaster",
    "Marine"
] = Field (description= 'mention drill type among this list only if its a valid drill')
 

parser_py = PydanticOutputParser(pydantic_object=Drill)

prompt1 = PromptTemplate(
    input_variables=['text'],
    template='check the {text} of drill description and classify the drill and find if its a valid drill.\n{format_instruction}',
    partial_variables={'format_instruction': parser_py.get_format_instructions()}
)

chain = prompt1 | model | parser_py

