from aiohttp import web
import uuid
from flask import jsonify
from uniflow.flow.client import TransformClient
from uniflow.flow.config import ExpandReduceConfig


class AsyncCall:
    """ Asynchronous Call of ExpandReduceFlow Class."""
    def __init__(self):
        pass

    def extract_input(self, input_str):
        """

        Args:
            input_str (str): The string format of the input dictionary

        Returns:
            Sequence[Mapping[str:Any]]: The sequence of input dictionary.
        """
        output = {}
        for i in range(0, len(input_str)):
            if input_str[i] == ":":
                output[str(input_str[i - 1])] = str(input_str[i + 1])
        return [output]

    async def async_expand_reduce(self, request):
        """Run flow.

        Args:
            request: the request from client

        Returns:
            Response: response json data to the client
        """
        # generate job id
        job_id = str(uuid.uuid4())

        try:
            # get input dictionary from request
            input_dict = request.query.get('input_dict')
            input_dict = self.extract_input(input_dict)

            # generate output node
            client = TransformClient(ExpandReduceConfig())
            output = await client.async_run(input_dict)
            print(output)

            # generate response data
            response_data = {'status': 'success', 'message': 'Async executed', 'job_id': job_id,
                             'result': output[0]["output"]}
            return web.json_response(response_data)

        except Exception as e:
            response_data = {'status': 'error', 'message': str(e)}
            return jsonify(response_data), 400


if __name__ == '__main__':
    async_call = AsyncCall()
    app = web.Application()
    app.router.add_get('/async-expand-reduce', async_call.async_expand_reduce)
    web.run_app(app)
