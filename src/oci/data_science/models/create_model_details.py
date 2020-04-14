# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateModelDetails(object):
    """
    Parameters needed to create a new model. Models are mathematical representations of the relationships between data. Models are represented by their associated metadata and artifact.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateModelDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateModelDetails.
        :type compartment_id: str

        :param project_id:
            The value to assign to the project_id property of this CreateModelDetails.
        :type project_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateModelDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateModelDetails.
        :type description: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateModelDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateModelDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'project_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'project_id': 'projectId',
            'display_name': 'displayName',
            'description': 'description',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._project_id = None
        self._display_name = None
        self._description = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateModelDetails.
        The `OCID`__ of the compartment to create the model in.

        __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/identifiers.htm


        :return: The compartment_id of this CreateModelDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateModelDetails.
        The `OCID`__ of the compartment to create the model in.

        __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateModelDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def project_id(self):
        """
        **[Required]** Gets the project_id of this CreateModelDetails.
        The `OCID`__ of the project to associate with the model.

        __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/identifiers.htm


        :return: The project_id of this CreateModelDetails.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this CreateModelDetails.
        The `OCID`__ of the project to associate with the model.

        __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/identifiers.htm


        :param project_id: The project_id of this CreateModelDetails.
        :type: str
        """
        self._project_id = project_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateModelDetails.
        A user-friendly display name for the resource. Does not have to be unique, and can be modified. Avoid entering confidential information.
        Example: `My Model`


        :return: The display_name of this CreateModelDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateModelDetails.
        A user-friendly display name for the resource. Does not have to be unique, and can be modified. Avoid entering confidential information.
        Example: `My Model`


        :param display_name: The display_name of this CreateModelDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateModelDetails.
        A short blurb describing the model.


        :return: The description of this CreateModelDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateModelDetails.
        A short blurb describing the model.


        :param description: The description of this CreateModelDetails.
        :type: str
        """
        self._description = description

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateModelDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateModelDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateModelDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateModelDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateModelDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateModelDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateModelDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateModelDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other