"""
Procedure Transformer

Transforms FHIR Procedure resources into an
analytics-ready Pandas DataFrame.
"""

from __future__ import annotations

from typing import Any

import pandas as pd

from src.transformation.base_transformer import BaseTransformer


class ProcedureTransformer(BaseTransformer):
    """
    Transform FHIR Procedure resources.
    """

    def transform(
        self,
        resources: list[dict[str, Any]],
    ) -> pd.DataFrame:
        """
        Transform Procedure resources into a DataFrame.
        """

        rows: list[dict[str, Any]] = []

        for procedure in resources:

            if procedure.get("resourceType") != "Procedure":
                continue

            performed_period = procedure.get(
                "performedPeriod",
                {},
            )

            rows.append(
                {
                    "procedure_id": procedure.get("id"),
                    "patient_id": self._extract_patient_id(
                        procedure
                    ),
                    "encounter_id": self._extract_encounter_id(
                        procedure
                    ),
                    "code_system": self._extract_code_system(
                        procedure
                    ),
                    "procedure_code": self._extract_procedure_code(
                        procedure
                    ),
                    "procedure_name": self._extract_procedure_name(
                        procedure
                    ),
                    "status": procedure.get("status"),
                    "performed_start": performed_period.get(
                        "start"
                    ),
                    "performed_end": performed_period.get(
                        "end"
                    ),
                    "location": self._extract_location(
                        procedure
                    ),
                }
            )

        return pd.DataFrame(rows)

    def _extract_patient_id(
        self,
        procedure: dict[str, Any],
    ) -> str | None:
        """
        Extract patient ID from subject.reference.
        """

        subject = procedure.get("subject", {})
        reference = subject.get("reference")

        return self._clean_reference(reference)

    def _extract_encounter_id(
        self,
        procedure: dict[str, Any],
    ) -> str | None:
        """
        Extract encounter ID from encounter.reference.
        """

        encounter = procedure.get("encounter", {})
        reference = encounter.get("reference")

        return self._clean_reference(reference)

    def _clean_reference(
        self,
        reference: str | None,
    ) -> str | None:
        """
        Convert FHIR references into clean IDs.
        """

        if not reference:
            return None

        if reference.startswith("urn:uuid:"):
            return reference.replace(
                "urn:uuid:",
                "",
                1,
            )

        return reference.split("/")[-1]

    def _extract_code_system(
        self,
        procedure: dict[str, Any],
    ) -> str | None:
        """
        Extract terminology system from Procedure.code.
        """

        coding = (
            procedure
            .get("code", {})
            .get("coding", [])
        )

        for item in coding:

            system = item.get("system")

            if system:
                return system

        return None

    def _extract_procedure_code(
        self,
        procedure: dict[str, Any],
    ) -> str | None:
        """
        Extract clinical procedure code.
        """

        coding = (
            procedure
            .get("code", {})
            .get("coding", [])
        )

        for item in coding:

            code = item.get("code")

            if code:
                return code

        return None

    def _extract_procedure_name(
        self,
        procedure: dict[str, Any],
    ) -> str | None:
        """
        Extract human-readable procedure name.
        """

        code = procedure.get("code", {})

        text = code.get("text")

        if text:
            return text

        coding = code.get("coding", [])

        for item in coding:

            display = item.get("display")

            if display:
                return display

        return None

    def _extract_location(
        self,
        procedure: dict[str, Any],
    ) -> str | None:
        """
        Extract procedure location display name.
        """

        location = procedure.get("location", {})

        return location.get("display")