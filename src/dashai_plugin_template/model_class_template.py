from DashAI.back.core.schema_fields import BaseSchema, schema_field
from DashAI.back.models.base_model import BaseModel


class ExampleModelSchema(BaseSchema):
    example_param_name: schema_field(  # Change example_param_name
        type_field(), # Choose between different types_fields e.g. int_field, string_field, etc
        placeholder=, # Placeholde to display in UI
        description=(
            "Field description"
        ),
    )  # type: ignore


class ExampleModelClass(
    # Add inheritances of abstract classes
    ):

    SCHEMA = ExampleModelSchema

    def __init__(self, **kwargs): # Params are passed when the model is initialized
        super().__init__(**kwargs)

    def fit(self, x_train, y_train) -> None: # x and y are DashAIDatasets (wrapper of dataset.Dataset)
        """ Fit the model to the data. It is necessary to put the trained model in self.model class variable

        Parameters
        ----------
        x_train : DashAIDatasets
            Input data.
        y_train : DashAIDatasets
            Output data.

        """
        raise NotImplementedError
    
    def predict(self, x_pred) -> list:
        """Make a prediction with the model.

        Parameters
        ----------
        x_pred : Union[DashAIDataset, pd.DataFrame]
            Dataset with the input data columns.

        Returns
        -------
        array-like
            Array with the predicted probabilities values for x_pred
        """
        raise NotImplementedError

    def save(self, filename: str) -> None:
        """Store an instance of a model.

        filename (Str): Indicates where to store the model,
        if filename is None, this method returns a bytes array with the model.
        """
        raise NotImplementedError
    
    @staticmethod
    def load(self, filename: str):
        """Restores an instance of a model.

        filename (Str): Indicates where the model was stored.
        """
        raise NotImplementedError
