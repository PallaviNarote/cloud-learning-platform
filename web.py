from flask import Flask, render_template, jsonify

app = Flask(__name__)

course_data = {

"cloud": {
"title": "Cloud Computing Fundamentals",
"text": """
<h2>What is Cloud Computing?</h2>

<b>Cloud computing</b> is a technology that allows users and organizations
to access computing resources such as <b>servers, storage, databases,
networking, and software</b> over the internet.

Instead of buying and maintaining physical hardware, companies can
<b>rent computing resources from cloud providers</b> and pay only for
what they use.

<hr>

<h2>Main Characteristics of Cloud Computing</h2>

<ul>
<li><b>On-Demand Self Service</b> – Users can create and manage resources automatically.</li>
<li><b>Broad Network Access</b> – Services are available through the internet and can be accessed from different devices.</li>
<li><b>Resource Pooling</b> – Cloud providers share computing resources among many users.</li>
<li><b>Rapid Elasticity</b> – Resources can be increased or decreased quickly.</li>
<li><b>Measured Service</b> – Users pay only for the resources they actually use.</li>
</ul>

<hr>

<h2>Service Models of Cloud Computing</h2>

<p><b>Infrastructure as a Service (IaaS)</b></p>
Provides virtual machines, storage, and networking.
Users manage operating systems and applications.

<p><b>Platform as a Service (PaaS)</b></p>
Provides a development platform where developers can build
and deploy applications without managing infrastructure.

<p><b>Software as a Service (SaaS)</b></p>
Provides ready-to-use applications that run in a web browser.

<hr>

<h2>Deployment Models</h2>

<ul>
<li><b>Public Cloud</b> – Cloud services shared among multiple organizations.</li>
<li><b>Private Cloud</b> – Cloud environment dedicated to a single organization.</li>
<li><b>Hybrid Cloud</b> – Combination of public and private cloud environments.</li>
</ul>

<hr>

<h2>Advantages of Cloud Computing</h2>

<ul>
<li><b>Lower cost</b> because hardware is not required.</li>
<li><b>High scalability</b> to handle changing workloads.</li>
<li><b>Global access</b> from anywhere in the world.</li>
<li><b>High reliability</b> due to distributed data centers.</li>
</ul>
"""
},

"aws": {
"title": "Amazon Web Services (AWS)",
"text": """
<h2>Introduction to AWS</h2>

<b>Amazon Web Services (AWS)</b> is one of the largest cloud
computing platforms in the world. It provides more than
<b>200 cloud services</b> for computing, storage, networking,
machine learning, security, and analytics.

AWS was launched by Amazon in <b>2006</b> and is widely used
by startups, enterprises, and government organizations.

<hr>

<h2>AWS Global Infrastructure</h2>

AWS uses a global network of data centers to provide reliable services.

<ul>
<li><b>Regions</b> – Physical geographic locations where AWS data centers exist.</li>
<li><b>Availability Zones</b> – Independent data centers inside a region.</li>
<li><b>Edge Locations</b> – Smaller data centers used for faster content delivery.</li>
</ul>

<hr>

<h2>Important AWS Services</h2>

<ul>
<li><b>Amazon EC2</b> – Virtual servers that run applications.</li>
<li><b>Amazon S3</b> – Highly scalable object storage service.</li>
<li><b>Amazon RDS</b> – Managed relational database service.</li>
<li><b>AWS Lambda</b> – Serverless computing that runs code without servers.</li>
</ul>

<hr>

<h2>Benefits of AWS</h2>

<ul>
<li><b>Highly scalable infrastructure</b></li>
<li><b>Secure cloud environment</b></li>
<li><b>Global network</b></li>
<li><b>Large variety of services</b></li>
</ul>

Many companies such as <b>Netflix, Airbnb, and Spotify</b>
run their applications on AWS infrastructure.
"""
},

"storage": {
"title": "Cloud Storage",
"text": """
<h2>What is Cloud Storage?</h2>

<b>Cloud storage</b> allows users to store data on remote servers
instead of storing files on local computers or physical drives.

The data is stored in large <b>cloud data centers</b> managed by
cloud providers and can be accessed through the internet.

<hr>

<h2>Advantages of Cloud Storage</h2>

<ul>
<li><b>Backup and recovery</b> – protects data from loss.</li>
<li><b>Global accessibility</b> – access files from anywhere.</li>
<li><b>High durability</b> – data is stored across multiple servers.</li>
<li><b>Scalability</b> – storage capacity can be increased easily.</li>
</ul>

<hr>

<h2>Types of Cloud Storage</h2>

<p><b>Object Storage</b></p>
Stores unstructured data such as images, videos, and documents.

<p><b>Block Storage</b></p>
Stores data in blocks and is commonly used for databases
and virtual machines.

<p><b>File Storage</b></p>
Provides shared file systems where multiple users
can access files simultaneously.

<hr>

<h2>Examples of Cloud Storage Services</h2>

<ul>
<li><b>Amazon S3</b></li>
<li><b>Google Cloud Storage</b></li>
<li><b>Microsoft Azure Blob Storage</b></li>
</ul>
"""
}

}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/lesson/<topic>")
def lesson(topic):
    return jsonify(course_data.get(topic))

if __name__ == "__main__":
    app.run(debug=True)