import views
from unittest.mock import MagicMock
from unittest import TestCase, mock

mock_connector_module = MagicMock()


class DBMUnitTest(TestCase):
    def test_select_query(self):
        # Arrange
        # Mock request function of POST and isolates it
        mock_request = MagicMock()
        mock_request.method = "POST"
        # Mocks render template
        mock_render_template = MagicMock()
        # Mocks cursor with execute and fetchall cursor statements
        mock_cursor = MagicMock()
        mock_cursor.execute = MagicMock(return_value=mock_cursor)
        mock_cursor.fetchall = MagicMock(return_value=[])
        # Mocks the database and cursor database
        mock_db = MagicMock()
        mock_db.cursor = MagicMock(return_value=mock_cursor)
        # Mocks the mysql connector for the database connection
        mock_connector_module.connect = MagicMock(return_value=mock_db)
        # Mocks instrument and serial number inputs to the form
        mock_request.form = {"instrument": "G2", "serial number": "12345678"}
        # Mocks flask request, render template, and mysql connector inputs
        with mock.patch("views.request", mock_request), (mock.patch("views.render_template",
            mock_render_template)), mock.patch("views.mysql.connector", mock_connector_module):
            # Act
            # Calls the service function in views
            views.service()

        # Assert
        # Mocks render template
        mock_render_template.assert_called_once_with("service.html", result=[])
