"""
Utilities for FHIR Observation resources.
"""

from __future__ import annotations

from typing import Any


class ObservationUtils:

    @staticmethod
    def extract_value(
        observation: dict[str, Any],
    ) -> tuple[str | float | int | None, str | None]:
        """
        Extract observation value and unit.
        """

        quantity = observation.get("valueQuantity")

        if quantity:
            return (
                quantity.get("value"),
                quantity.get("unit"),
            )

        string_value = observation.get("valueString")

        if string_value:
            return string_value, None

        concept = observation.get(
            "valueCodeableConcept"
        )

        if concept:

            text = concept.get("text")

            if text:
                return text, None

            coding = concept.get("coding", [])

            if coding:
                return (
                    coding[0].get("display")
                    or coding[0].get("code"),
                    None,
                )

        return None, None