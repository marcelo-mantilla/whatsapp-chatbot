import json


def create_calendar_event_function():
    return {
        'name': 'create_calendar_event',
        'description': 'Creates a google calendar event with the given parameters',
        'parameters': {
            'type': 'object',
            'properties': {
                'summary': {
                    'type': 'string',
                    'description': 'The title of the calendar event.'
                },
                'location': {
                    'type': 'string',
                    'description': 'Geographic location of the event as free-form text. Optional.',
                },
                'description': {
                    'type': 'string',
                    'description': 'Positive and concise description of the event. Can be user specified.'
                },
                'start': {
                    'type': 'object',
                    'properties': {
                        'dateTime': {
                            'type': 'string',
                            'description': 'The time, as a combined date-time value (formatted according to RFC3339). '
                                           'A time zone offset is required. Ask the user if you do not know the time '
                                           'zone.'
                        },
                    }
                },
                'end': {
                    'type': 'object',
                    'properties': {
                        'dateTime': {
                            'type': 'string',
                            'description': 'The time, as a combined date-time value (formatted according to RFC3339). '
                                           'A time zone offset is required. Ask the user if you do not know the time '
                                           'zone.',
                        },
                    }
                },
                'attendees': {
                    'type': 'array',
                    'properties': {
                        'email': {
                            'type': 'string',
                            'description': 'The emails of the attendees of the event.',
                        },
                        'displayName': {
                            'type': 'string',
                            'description': 'The display name of the attendee. Optional.',
                        }

                    }
                }
            }
        }
    }


# This is a GET request, adapt to query parameters
def get_events_list_function():
    return {
        'name': 'get_events_list',
        'description': 'Returns a list of events from the user\'s calendar',
        'parameters': {
            'type': 'object',
            'properties': {
                'timeMin': {
                    'type': 'string',
                    'description': 'Lower bound (exclusive) for an events end time to filter by. Optional. The '
                                   'default is not to filter by end time. Must be an RFC3339 timestamp with mandatory '
                                   'time zone offset, for example, 2011-06-03T10:00:00-07:00, 2011-06-03T10:00:00Z. '
                                   'Milliseconds may be provided but are ignored. If timeMax is set, timeMin must be '
                                   'smaller than timeMax.'
                },
                'timeMax': {
                    'type': 'string',
                    'description': 'Upper bound (exclusive) for an events start time to filter by. Optional. The '
                                   'default is not to filter by start time. Must be an RFC3339 timestamp with '
                                   'mandatory time zone offset, for example, 2011-06-03T10:00:00-07:00, '
                                   '2011-06-03T10:00:00Z. Milliseconds may be provided but are ignored. If timeMin is '
                                   'set, timeMax must be greater than timeMin.'
                },
            }
        }
    }
