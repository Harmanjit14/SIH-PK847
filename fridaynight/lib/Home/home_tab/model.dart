class InstituteEvent {
  String? id,
      eventName,
      startDate,
      endDate,
      overview,
      description,
      hostName,
      hostContact;

  fromJson(var data) {
    id = data['id'];
    hostContact = data['hostContact'];
    hostName = data['hostName'];
    overview = data['eventOverview'];
    description = data['eventDescription'];
    eventName = data['eventName'];
    startDate = data['startDate'];
    endDate = data['endDate'];
  }
}

class StudentParticipation {
  String? id, eventName, eventId;

  fromJson(var data){
    id = data['id'];
    eventName = data['event']['eventName'];
    eventId = data['event']['id'];
  }
}
