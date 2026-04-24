from mangum import Mangum
from server import app

# Create the Lambda handler ---- Lambda function entry point
handler = Mangum(app)