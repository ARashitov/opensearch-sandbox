import json
import typing as tp


def serialize(message: dict[str, tp.Any]) -> bytearray:
    return json.dumps(message).encode('ascii')


def deserialize(message: bytearray) -> dict[str, tp.Any]:
    return json.loads(message.decode('ascii'))
