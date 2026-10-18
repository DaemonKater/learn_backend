class Appointment:
    def __init__(self, id: int, client_name: str, master_id: int, service_id: int, time: str):
        self.id = id
        self.client_name = client_name
        self.master_id = master_id
        self.service_id = service_id
        self.time = time


Appoinment = Appointment

appointments = []


def create_appointment(
    client_name: str,
    master_id: int,
    service_id: int,
    time: str,
) -> Appointment | None:
    if not client_name or master_id is None or service_id is None or not time:
        return None

    if not ("08:00" <= time <= "20:00"):
        return None

    master = get_master(master_id)
    service = get_service(service_id)

    if master is None or service is None:
        return None

    appointment = Appointment(
        id=len(appointments) + 1,
        client_name=client_name,
        master_id=master.master_id,
        service_id=service.service_id,
        time=time,
    )
    appointments.append(appointment)
    return appointment


class Master:
    def __init__(self, master_id: int):
        self.master_id = master_id


class Service:
    def __init__(self, service_id: int):
        self.service_id = service_id


def get_master(master_id: int):
    return Master(master_id) if master_id else None


def get_service(service_id: int):
    return Service(service_id) if service_id else None


if __name__ == "__main__":
    first_appointment = create_appointment("Иванова А.А.", 1, 1, "10:00")
    second_appointment = create_appointment("Петрова А.А.", 1, 1, "11:00")

    print("Список записей:")
    for appointment in appointments:
        print(appointment.client_name, appointment.time)

    no_correct_appointment_1 = create_appointment("", 1, 1, "12:00")
    print("Пустое имя:", no_correct_appointment_1)

    no_correct_appointment_2 = create_appointment("Сидорова А.А.", 1, 1, "00:00")
    print("Некорректное время:", no_correct_appointment_2)

    print("Всего корректных записей в списке:", len(appointments))