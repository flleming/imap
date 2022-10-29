from rocketry import Rocketry
from rocketry.args import FuncArg
from service.request import generateRequest
from rocketry.conds import daily, every
app = Rocketry(execution='async')


@app.task(daily, execution='async')
async def create_request(createRequest=FuncArg(generateRequest)):
    next(createRequest)

