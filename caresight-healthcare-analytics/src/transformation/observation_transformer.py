"""
Observation Transformer

Transforms FHIR Observation resources into an
analytics-ready Pandas DataFrame.
"""

from __future__ import annotations

from typing import Any

import pandas as pd

from src.transformation.base_transformer import BaseTransformer
from src.utils.observation_utils import ObservationUtils


class ObservationTransformer(BaseTransformer):
    """
    Transform FHIR Observation resources.
    """

    def transform(
        self,
        resources: list[dict[str, Any]],
    ) -> pd.DataFrame:
        """
        Transform Observation FHIR resources into a DataFrame.
        """

        rows: list[dict[str, Any]] = []

        for observation in resources:

            # We already receive Observation resources,
            # but this protects the transformer from mixed input.
            if observation.get("resourceType") != "Observation":
                continue

            value, unit = ObservationUtils.extract_value(
                observation
            )

            row = {
                "observation_id": observation.get("id"),
                "patient_id": self._extract_patient_id(
                    observation
                ),
                "encounter_id": self._extract_encounter_id(
                    observation
                ),
                "loinc_code": self._extract_loinc_code(
                    observation
                ),
                "observation_name": self._extract_observation_name(
                    observation
                ),
                "value": value,
                "unit": unit,
                "status": observation.get("status"),
                "effective_datetime": observation.get(
                    "effectiveDateTime"
                ),
            }

            rows.append(row)

        return pd.DataFrame(rows)

    def _extract_patient_id(
        self,
        observation: dict[str, Any],
    ) -> str | None:
        """
        Extract patient ID from Observation.subject.reference.
        """

        subject = observation.get("subject", {})

        reference = subject.get("reference")

        if not reference:
            return None

        if reference.startswith("urn:uuid:"):
            return reference.replace(
                "urn:uuid:",
                "",
                1,
            )

        return reference.split("/")[-1]

    def _extract_encounter_id(
        self,
        observation: dict[str, Any],
    ) -> str | None:
        """
        Extract encounter ID from Observation.encounter.reference.
        """

        encounter = observation.get("encounter", {})

        reference = encounter.get("reference")

        if not reference:
            return None

        if reference.startswith("urn:uuid:"):
            return reference.replace(
                "urn:uuid:",
                "",
                1,
            )

        return reference.split("/")[-1]

    def _extract_loinc_code(
        self,
        observation: dict[str, Any],
    ) -> str | None:
        """
        Extract the LOINC code from Observation.code.
        """

        coding = (
            observation
            .get("code", {})
            .get("coding", [])
        )

        for code in coding:

            if code.get("system") == "http://loinc.org":
                return code.get("code")

        return None

    def _extract_observation_name(
        self,
        observation: dict[str, Any],
    ) -> str | None:
        """
        Extract the human-readable observation name.
        """

        code = observation.get("code", {})

        text = code.get("text")

        if text:
            return text

        coding = code.get("coding", [])

        for item in coding:

            display = item.get("display")

            if display:
                return display

        return None
            
            
            
    