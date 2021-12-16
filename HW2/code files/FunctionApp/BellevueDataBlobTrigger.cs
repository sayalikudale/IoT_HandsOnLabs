using System;
using System.IO;
using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Host;
using Microsoft.Extensions.Logging;

namespace uw.Function
{
    public static class BellevueDataBlobTrigger
    {
        [FunctionName("BellevueDataBlobTrigger")]
        public static void Run([BlobTrigger("container1/{name}", Connection = "bellevuestorageaccount_STORAGE")]Stream myBlob, string name, ILogger log)
        {
            log.LogInformation($"C# Blob trigger function Processed blob\n Name:{name} \n Size: {myBlob.Length} Bytes");

            //read the blob stream data
            StreamReader reader = new StreamReader(myBlob);
            string  oldContent = reader.ReadToEnd();
            log.LogInformation(oldContent);

        }
    }
}
