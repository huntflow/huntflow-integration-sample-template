from fastapi import APIRouter, Body, Depends

from hf_integration_sample.api.controllers.applicant_hook import process_applicant_hook
from hf_integration_sample.api.serializers.response.hf_hook import HFHookResponse
from hf_integration_sample.api.serializers.request.applicant_hook import (
    ApplicantHookRequest,
)
from hf_integration_sample.app.hf_hooks import hf_hooks_auth


router = APIRouter(dependencies=[Depends(hf_hooks_auth)])


@router.post("/applicant_hook", response_model=HFHookResponse)
async def applicant_hook(
    data: ApplicantHookRequest = Body(..., description="Request body"),
):
    response = {"status": "ok"}
    await process_applicant_hook(data)
    return response
