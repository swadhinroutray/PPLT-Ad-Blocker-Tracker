//* Parse data
const fse = require("fs-extra");
//! Change filepath with the right parsed folder
const filepath = "../data/parsed/Ublock_Edge";
async function getAverageTimes() {
  var files = await fse.readdir(filepath);
  console.log(files.length);
  let totalDistinctRequests = 0;
  let totalMedianTime = 0;
  let totalNinetyFifthTime = 0;
  let maxCallsToTopURL = 0;
  let longestURLCall = 0;

  for (let index = 0; index < files.length; index++) {
    const file = files[index];
    var data = await fse.readFile(filepath + "/" + file, "utf8");
    var contents = JSON.parse(data);
    var filteredContent = contents.requests;
    // console.log(filteredContent);
    totalDistinctRequests += filteredContent.all.noOfRequests;
    totalMedianTime += filteredContent.all.medianTime;
    totalNinetyFifthTime += filteredContent.all.ninetyFifthTime;
    maxCallsToTopURL += filteredContent.all.topUrl.noOfOccurrences;
    longestURLCall += filteredContent.all.longest.time;
  }
  const structureData = [
    {
      Result: "Average Distinct Requests",
      Value: totalDistinctRequests / files.length,
    },
    {
      Result: "Average Median Time",
      Value: totalMedianTime / files.length,
    },
    {
      Result: "Average NinetyFith Time",
      Value: totalNinetyFifthTime / files.length,
    },
    {
      Result: "Average Maximum Calls to Top URL",
      Value: maxCallsToTopURL / files.length,
    },
    {
      Result: "Average Longest URL Call",
      Value: longestURLCall / files.length,
    },
  ];
  console.table(structureData);
}

getAverageTimes();
