import logging
import azure.functions as func
import math


def calculate_displacement(engine_bore, engine_stroke, engine_cylinders):
    # calculate and round the engine displacement
    engine_displacement = math.pi / 4 * engine_bore**2 * engine_stroke * engine_cylinders
    engine_displacement = round(engine_displacement, 3)
    return engine_displacement



def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info(f"HTTP trigger executed!")
    
    # name = req.params.get('name')
    engine_bore = req.params.get('engine_bore')
    engine_stroke = req.params.get('engine_stroke')
    engine_cylinders = req.params.get('engine_cylinders')
    
    if not engine_bore:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            engine_bore = req_body.get('engine_bore')

    if not engine_stroke:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            engine_stroke = req_body.get('engine_stroke')

    if not engine_cylinders:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            engine_cylinders = req_body.get('engine_cylinders')

    if engine_bore and engine_stroke and engine_cylinders:
        displacement = calculate_displacement(float(engine_bore), float(engine_stroke), float(engine_cylinders))
        return func.HttpResponse(f"Displacement: {displacement}.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. However, one or more of the required params are missing.",
             status_code=200
        )
