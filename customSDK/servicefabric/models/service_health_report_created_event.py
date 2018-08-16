# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .service_event import ServiceEvent


class ServiceHealthReportCreatedEvent(ServiceEvent):
    """Service Health Report Created event.

    :param event_instance_id: The identifier for the FabricEvent instance.
    :type event_instance_id: str
    :param time_stamp: The time event was logged.
    :type time_stamp: datetime
    :param has_correlated_events: Shows there is existing related events
     available.
    :type has_correlated_events: bool
    :param kind: Constant filled by server.
    :type kind: str
    :param service_id: The identity of the service. This ID is an encoded
     representation of the service name. This is used in the REST APIs to
     identify the service resource.
     Starting in version 6.0, hierarchical names are delimited with the "\\~"
     character. For example, if the service name is "fabric:/myapp/app1/svc1",
     the service identity would be "myapp~app1\\~svc1" in 6.0+ and
     "myapp/app1/svc1" in previous versions.
    :type service_id: str
    :param instance_id: Id of Service instance.
    :type instance_id: long
    :param source_id: Id of report source.
    :type source_id: str
    :param property: Describes the property.
    :type property: str
    :param health_state: Describes the property health state.
    :type health_state: str
    :param time_to_live_ms: Time to live in milli-seconds.
    :type time_to_live_ms: long
    :param sequence_number: Sequence number of report.
    :type sequence_number: long
    :param description: Description of report.
    :type description: str
    :param remove_when_expired: Indicates the removal when it expires.
    :type remove_when_expired: bool
    :param source_utc_timestamp: Source time.
    :type source_utc_timestamp: datetime
    """

    _validation = {
        'event_instance_id': {'required': True},
        'time_stamp': {'required': True},
        'kind': {'required': True},
        'service_id': {'required': True},
        'instance_id': {'required': True},
        'source_id': {'required': True},
        'property': {'required': True},
        'health_state': {'required': True},
        'time_to_live_ms': {'required': True},
        'sequence_number': {'required': True},
        'description': {'required': True},
        'remove_when_expired': {'required': True},
        'source_utc_timestamp': {'required': True},
    }

    _attribute_map = {
        'event_instance_id': {'key': 'EventInstanceId', 'type': 'str'},
        'time_stamp': {'key': 'TimeStamp', 'type': 'iso-8601'},
        'has_correlated_events': {'key': 'HasCorrelatedEvents', 'type': 'bool'},
        'kind': {'key': 'Kind', 'type': 'str'},
        'service_id': {'key': 'ServiceId', 'type': 'str'},
        'instance_id': {'key': 'InstanceId', 'type': 'long'},
        'source_id': {'key': 'SourceId', 'type': 'str'},
        'property': {'key': 'Property', 'type': 'str'},
        'health_state': {'key': 'HealthState', 'type': 'str'},
        'time_to_live_ms': {'key': 'TimeToLiveMs', 'type': 'long'},
        'sequence_number': {'key': 'SequenceNumber', 'type': 'long'},
        'description': {'key': 'Description', 'type': 'str'},
        'remove_when_expired': {'key': 'RemoveWhenExpired', 'type': 'bool'},
        'source_utc_timestamp': {'key': 'SourceUtcTimestamp', 'type': 'iso-8601'},
    }

    def __init__(self, event_instance_id, time_stamp, service_id, instance_id, source_id, property, health_state, time_to_live_ms, sequence_number, description, remove_when_expired, source_utc_timestamp, has_correlated_events=None):
        super(ServiceHealthReportCreatedEvent, self).__init__(event_instance_id=event_instance_id, time_stamp=time_stamp, has_correlated_events=has_correlated_events, service_id=service_id)
        self.instance_id = instance_id
        self.source_id = source_id
        self.property = property
        self.health_state = health_state
        self.time_to_live_ms = time_to_live_ms
        self.sequence_number = sequence_number
        self.description = description
        self.remove_when_expired = remove_when_expired
        self.source_utc_timestamp = source_utc_timestamp
        self.kind = 'ServiceHealthReportCreated'
