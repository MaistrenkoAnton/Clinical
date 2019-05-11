from django.contrib import admin
from django.contrib.admin import ModelAdmin

from initial import models


@admin.register(models.BaselineCounts)
class BaselineCountsAdmin(ModelAdmin):
    list_display = ('units', 'scope', 'ctgov_group_code')


@admin.register(models.BaselineMeasurements)
class BaselineMeasurementsCountsAdmin(ModelAdmin):
    list_display = (
        'result_group', 'ctgov_group_code', 'classification',
        'category', 'title', 'description', 'dispersion_type',
        'units', 'param_type', 'param_value', 'dispersion_value',
        'explanation_of_na'
    )


@admin.register(models.BriefSummaries)
class BriefSummariesAdmin(ModelAdmin):
    list_display = ('description',)


@admin.register(models.BrowseConditions)
class BrowseConditionsAdmin(ModelAdmin):
    list_display = ('mesh_term', 'downcase_mesh_term')


@admin.register(models.BrowseInterventions)
class BrowseInterventionsAdmin(ModelAdmin):
    list_display = ('mesh_term', 'downcase_mesh_term')


@admin.register(models.CalculatedValues)
class CalculatedValuesAdmin(ModelAdmin):
    list_display = ('minimum_age_unit', 'maximum_age_unit')


@admin.register(models.CentralContacts)
class CentralContactsAdmin(ModelAdmin):
    list_display = ('name', 'phone', 'email', 'contact_type')


@admin.register(models.Conditions)
class ConditionsAdmin(ModelAdmin):
    list_display = ('name', 'downcase_name',)


@admin.register(models.Countries)
class CountriesAdmin(ModelAdmin):
    list_display = ('name',)


@admin.register(models.DesignGroupInterventions)
class DesignGroupInterventionsAdmin(ModelAdmin):
    pass


@admin.register(models.DesignGroups)
class DesignGroupsAdmin(ModelAdmin):
    list_display = ('group_type', 'title', 'description')


@admin.register(models.DesignOutcomes)
class DesignOutcomesAdmin(ModelAdmin):
    list_display = (
        'outcome_type', 'measure', 'time_frame',
        'population', 'description',
    )


@admin.register(models.Designs)
class DesignsAdmin(ModelAdmin):
    list_display = (
        'allocation', 'intervention_model', 'observational_model',
        'primary_purpose', 'time_perspective', 'masking',
        'masking_description', 'intervention_model_description',
    )


@admin.register(models.DetailedDescriptions)
class DetailedDescriptionsAdmin(ModelAdmin):
    list_display = ('description',)


@admin.register(models.Documents)
class DocumentsAdmin(ModelAdmin):
    list_display = ('document_type', 'document_id', 'url', 'comment')


@admin.register(models.DropWithdrawals)
class DropWithdrawalsAdmin(ModelAdmin):
    list_display = ('ctgov_group_code', 'period', 'reason')


@admin.register(models.Eligibilities)
class EligibilitiesAdmin(ModelAdmin):
    list_display = (
        'sampling_method', 'gender', 'minimum_age', 'maximum_age',
        'healthy_volunteers', 'gender', 'population', 'criteria',
        'gender_description',
    )


@admin.register(models.Facilities)
class FacilitiesAdmin(ModelAdmin):
    list_display = ('status', 'name', 'city', 'state', 'zip', 'country')


@admin.register(models.FacilityContacts)
class FacilityContactsAdmin(ModelAdmin):
    list_display = ('contact_type', 'name', 'email', 'phone')


@admin.register(models.FacilityInvestigators)
class FacilityInvestigatorsAdmin(ModelAdmin):
    list_display = ('role', 'name',)


@admin.register(models.IdInformation)
class IdInformationAdmin(ModelAdmin):
    list_display = ('id_type', 'id_value')


@admin.register(models.InterventionOtherNames)
class InterventionOtherNamesAdmin(ModelAdmin):
    list_display = ('name',)


@admin.register(models.Interventions)
class InterventionsAdmin(ModelAdmin):
    list_display = ('name', 'description', 'intervention_type')


@admin.register(models.IpdInformationTypes)
class IpdInformationTypesAdmin(ModelAdmin):
    list_display = ('name',)


@admin.register(models.Keywords)
class KeywordsAdmin(ModelAdmin):
    list_display = ('name', 'downcase_name')


@admin.register(models.Links)
class LinksAdmin(ModelAdmin):
    list_display = ('url', 'description')


@admin.register(models.MeshHeadings)
class MeshHeadingsAdmin(ModelAdmin):
    list_display = ('heading', 'qualifier', 'subcategory')


@admin.register(models.MeshTerms)
class MeshTermsAdmin(ModelAdmin):
    list_display = ('qualifier', 'tree_number', 'description', 'mesh_term', 'downcase_mesh_term')


@admin.register(models.Milestones)
class MilestonesAdmin(ModelAdmin):
    list_display = ('ctgov_group_code', 'title', 'period', 'description')


@admin.register(models.OutcomeAnalyses)
class OutcomeAnalysesAdmin(ModelAdmin):
    list_display = ('non_inferiority_type', 'non_inferiority_description',
                    'param_type', 'param_value', 'dispersion_type',
                    'method', 'method_description')


@admin.register(models.OutcomeAnalysisGroups)
class OutcomeAnalysisGroupsAdmin(ModelAdmin):
    list_display = ('ctgov_group_code',)


@admin.register(models.OutcomeCounts)
class OutcomeCountsAdmin(ModelAdmin):
    list_display = ('ctgov_group_code', 'scope', 'units')


@admin.register(models.OutcomeMeasurements)
class OutcomeMeasurementsAdmin(ModelAdmin):
    list_display = ('title', 'category', 'classification', 'ctgov_group_code')


@admin.register(models.Outcomes)
class OutcomesAdmin(ModelAdmin):
    list_display = ('outcome_type', 'title', 'description', 'time_frame', 'population')


@admin.register(models.OverallOfficials)
class OverallOfficialsAdmin(ModelAdmin):
    list_display = ('role', 'name', 'affiliation')


@admin.register(models.ParticipantFlows)
class ParticipantFlowsAdmin(ModelAdmin):
    list_display = ('recruitment_details', 'pre_assignment_details')


@admin.register(models.PendingResults)
class PendingResultsAdmin(ModelAdmin):
    list_display = ('event', 'event_date_description')


@admin.register(models.ProvidedDocuments)
class ProvidedDocumentsAdmin(ModelAdmin):
    list_display = ('document_type', 'url')


@admin.register(models.ReportedEvents)
class ReportedEventsAdmin(ModelAdmin):
    list_display = ('ctgov_group_code', 'time_frame', 'event_type',
                    'default_vocab', 'default_assessment', 'description')


@admin.register(models.ResponsibleParties)
class ResponsiblePartiesAdmin(ModelAdmin):
    list_display = ('responsible_party_type', 'name', 'title', 'organization',
                    'affiliation')


@admin.register(models.ResultAgreements)
class ResultAgreementsAdmin(ModelAdmin):
    list_display = ('pi_employee', 'agreement')


@admin.register(models.ResultContacts)
class ResultContactsAdmin(ModelAdmin):
    list_display = ('organization', 'name', 'phone', 'email')


@admin.register(models.ResultGroups)
class ResultGroupsAdmin(ModelAdmin):
    list_display = ('ctgov_group_code', 'result_type', 'title', 'description')


@admin.register(models.Sponsors)
class SponsorsAdmin(ModelAdmin):
    list_display = ('agency_class', 'name', 'lead_or_collaborator')


@admin.register(models.StudyReferences)
class StudyReferencesAdmin(ModelAdmin):
    pass
