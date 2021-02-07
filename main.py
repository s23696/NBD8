import riak


class Main:
    def __init__(self):
        self.client = self.connectClient()
        self.bucket = self.createBucket("test")

    def connectClient(self):
        client = riak.RiakClient(pb_port=8087, protocol='pbc')
        return client

    def createBucket(self, name):
        myBucket = self.client.bucket(name)
        return myBucket

    def uploadValue(self,key ,value):
        print("Uploading value: " + str(value) + " to object with key: " + key)
        bucketObject = self.bucket.new(key, data=value)
        bucketObject.store()

    def getValue(self, key):
        fetched = self.bucket.get(key)
        print("The value of the object with key: " + key +" is: " + str(fetched.data))

    def deleteObject(self, key):
        print("RiakObject with key: " + key + " was deleted")
        self.bucket.delete(key)



    def run(self):
        self.connectClient()
        self.createBucket("test")

        self.uploadValue("keyOne", "1")
        self.getValue("keyOne")
        self.uploadValue("keyOne", "2")
        self.getValue("keyOne")
        self.deleteObject("keyOne")
        self.getValue("keyOne")


app = Main()
app.run()
