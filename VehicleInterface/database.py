import json
from django.core.serializers.json import DjangoJSONEncoder
from VehicleInterface.models import NavicationRecord, Vehicle
import logging
logger = logging.getLogger(__name__)


def last_point():
    logger.info("Getting last point information.")

    last_point = []
    temp_last_point_dict = {}

    try:
        query_last_point = NavicationRecord.objects.\
            values_list('latitude', 'longitude', 'date_time', "vehicle__plate").all()
    except Exception as error:
        logger.info("ERROR while getting last point information!\n ", error)
    else:
        for each_last_point_val in query_last_point:
            temp_last_point_dict['latitude'] = str(each_last_point_val[0])
            temp_last_point_dict['longitude'] = str(each_last_point_val[1])
            temp_last_point_dict['date_time'] = str(each_last_point_val[2])
            temp_last_point_dict['vehicle_plate'] = str(each_last_point_val[3])

            last_point.append(temp_last_point_dict)
            temp_last_point_dict = {}

        logger.info("Last point information getting process finish successfully.")

    return last_point


def fill_report_table(selected_date):
    selected_date = selected_date[6:10] + '-' + selected_date[0:2] + '-' + selected_date[3:5]
    logger.info("Getting report table informations.")
    try:
        table_informations = NavicationRecord.objects.\
            values_list('vehicle__driver_id__operation__name', 'vehicle__vehicle_location', 'date_time',
                        'vehicle__driver_id__name', 'vehicle__driver_id__driver_performance',
                        'vehicle__driver_id__operation__status').\
            filter(date_time=selected_date).all()

        json_table_informations = json.dumps(
            {"key_table_informations": list(table_informations)},
            cls=DjangoJSONEncoder
        )
    except Exception as error:
        logger.info("ERROR while getting report table informations! \n", error)
        return error
    else:
        return json_table_informations


def get_vehicle():
    vehicles = Vehicle.objects.values_list('vehicle_location')

    logger.debug("Araclar: %s", str(vehicles))

    return vehicles

