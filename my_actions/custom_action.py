import aiohttp
from asyncflows import Action, BaseModel, Field
from asyncflows.log_config import get_logger
import os

log = get_logger()

api_base= os.getenv('api_base')

class Inputs(BaseModel):
    role: str = Field(
        description="The Job title the candidate is interested in"
    )
    resume_text: str = Field(
        description="The resume of the candidate"
    )
    job_description: str = Field(
        description="The description of the job the candidate is interested in"
    )
    name: str = Field(
        description="The Name of the candidate applying for the job"
    )
    hiring_manager: str = Field(
        description="The hiring manager of the company"
    )
    referral: str = Field(
        description="Where the candidate learned about the job vacancy"
    )
    company: str = Field(
        description="The Company which the candidate wants to work in"
    )
    cand_address: str = Field(
        description="The address of the candidate"
    )
    comp_address: str = Field(
        description="The address of the company"
    )

class Outputs(BaseModel):
    cover_letter: str = Field(
        description="The generated cover letter"
    )

# Define your custom action class
class GenerateCoverLetter(Action[Inputs, Outputs]):
    name = 'generate_cover_letter'

    async def run(self, inputs: Inputs) -> Outputs:
        async with aiohttp.ClientSession() as session:
            url = 'api_base'
            async with session.get(url) as response:
                cover_letter = await response.text()

        return Outputs(cover_letter=cover_letter)
