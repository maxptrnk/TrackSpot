

function user_genres_proportions_doughnut(labels,values){


    var genresDoughnut = document.getElementById('genresDoughnut').getContext('2d');                
    new Chart(genresDoughnut, {
        type: 'doughnut',
        data: {
            labels: labels,

            datasets: [{
                label: 'My First Dataset',
                data: values,
                backgroundColor: [
                    'rgb(255, 99, 132)',
                    'rgb(54, 162, 235)',
                    'rgb(255, 205, 86)',
                    'rgb(54, 162, 11)',
                    'rgb(255, 11, 86)',
                    'rgb(0, 110, 16)',],
                
                borderColor: [
                    'rgb(255, 99, 132)',
                    'rgb(54, 162, 235)',
                    'rgb(255, 205, 86)',
                    'rgb(54, 162, 11)',
                    'rgb(255, 11, 86)',
                    'rgb(0, 110, 16)',],

            hoverOffset: 4
            }]},
        });
//   <script> const myChart = new Chart(document.getElementById('myChart'),config); </script>
}



function radar_graph(user_data, spotify_data){


    var radarChart = document.getElementById('radarChart').getContext('2d');

    new Chart(radarChart, {

        type: 'radar',
        
        data: {
            labels: ['Danceability', 'Energy', 'Acousticness', 'Speechiness', 'Valence', "Instrumentalness"],

            datasets: [{
              data: user_data,
              backgroundColor: ['rgba(127, 239, 189, 0.5)'],
              borderColor: ['rgba(97, 199, 159, 0.97)'],
              borderWidth: 2,
              label: "You",
              pointBackgroundColor: "rgba(127, 239, 189, 0.63)"
          },{
                data: spotify_data,
                backgroundColor: ['rgba(255, 255, 255, 0.5)'],
                borderColor: ['rgba(255, 255, 255, 0.97)'],
                borderWidth: 2,
                label: "Top Spotify Songs in 2020",
                pointBackgroundColor: "rgba(91, 75, 73, 0.63)"
            }, 
            
            ]
            }, 

        options: {
            scales:{
                r:{
                    angleLines: {
                        color:'white'
                    },
                    grid: {
                        color: ['rgba(147, 124, 33, 0.67)']
                    },  
                    pointLabels:{
                        color:'white',
                        font: {size : 18}
                    },
                    ticks:{
                        color:'white',
                        backdropColor: "#0c0b09"
                    },
                }
            }
            }

        });
}


function bar_graph(data_recent, data_mid, data_long){


    var barChart = document.getElementById('barChart').getContext('2d');

    new Chart(barChart, {

        type: 'bar',
        
        data: {
            labels: ['Recent', 'Mid-Term', 'Long-Term'],

            datasets: [{
                        data: [data_recent[0],data_mid[0],data_long[0]],
                        backgroundColor: ['rgba(91, 75, 73, 1)'],
                        borderWidth: 2,
                        label: "Danceability",
                        pointBackgroundColor: "rgba(169, 4, 23, 0.63)"
                        },{
                        data: [data_recent[1],data_mid[1],data_long[1]],
                        backgroundColor: ['rgba(219, 147, 176,1)'],
                        borderWidth: 2,
                        label: "Energy",
                        pointBackgroundColor: "rgba(26, 169, 4, 0.63)"
                        },{
                        data: [data_recent[2],data_mid[2],data_long[2]],
                        backgroundColor: ['rgba(247, 191, 180,1)'],
                        borderWidth: 2,
                        label: "Acousticness",
                        pointBackgroundColor: "rgba(26, 169, 4, 0.63)"
                      },{
                        data: [data_recent[3],data_mid[3],data_long[3]],
                        backgroundColor: ['rgba(125, 175, 156,1)'],
                        borderWidth: 2,
                        label: "Speechiness",
                        pointBackgroundColor: "rgba(26, 169, 4, 0.63)"
                      },{
                        data: [data_recent[4],data_mid[4],data_long[4]],
                        backgroundColor: ['rgba(35, 150, 127,1)'],
                        borderWidth: 2,
                        label: "Valence",
                        pointBackgroundColor: "rgba(26, 169, 4, 0.63)"
                      },{
                        data: [data_recent[5],data_mid[5],data_long[5]],
                        backgroundColor: ['rgba(127, 239, 189,1)'],
                        borderWidth: 2,
                        label: "Instrumentalness",
                        pointBackgroundColor: "rgba(26, 169, 4, 0.63)"
                        }]
            }, 


        });
}


//     cols = ['Danceability', 'Energy', 'Acousticness', 'Speechiness', 'Valence', 'Instrumentalness']








const words = [
    { key: "word", value: 10 },
    { key: "words", value: 8 },
    { key: "sprite", value: 7 },
    { key: "placed", value: 5 },
    { key: "layout", value: 4 },
    { key: "algorithm", value: 4 },
    { key: "area", value: 4 },
    { key: "without", value: 3 },
    { key: "step", value: 3 },
    { key: "bounding", value: 3 },
    { key: "retrieve", value: 3 },
    { key: "operation", value: 3 },
    { key: "collision", value: 3 },
    { key: "candidate", value: 3 },
    { key: "32", value: 2 },
    { key: "placement", value: 2 },
    { key: "time", value: 2 },
    { key: "possible", value: 2 },
    { key: "even", value: 2 },
    { key: "simple", value: 2 },
    { key: "starting", value: 2 },
    { key: "previously", value: 2 },
    { key: "move", value: 2 },
    { key: "perform", value: 2 },
    { key: "hierarchical", value: 2 },
    { key: "draw", value: 2 },
    { key: "pixel", value: 2 },
    { key: "data", value: 2 },
    { key: "separately", value: 2 },
    { key: "expensive", value: 2 },
    { key: "pixels", value: 2 },
    { key: "masks", value: 2 },
    { key: "implementation", value: 2 },
    { key: "detection", value: 2 },
    { key: "larger", value: 2 },
    { key: "whole", value: 2 },
    { key: "comparing", value: 2 },
    { key: "box", value: 2 },
    { key: "large", value: 2 },
    { key: "think", value: 2 },
    { key: "version", value: 2 },
    { key: "single", value: 2 },
    { key: "tree", value: 2 },
    { key: "Cloud", value: 1 },
    { key: "Generator", value: 1 },
    { key: "Works", value: 1 },
    { key: "positioning", value: 1 },
    { key: "overlap", value: 1 },
    { key: "available", value: 1 },
    { key: "GitHub", value: 1 },
    { key: "open", value: 1 },
    { key: "source", value: 1 },
    { key: "license", value: 1 },
    { key: "d3cloud", value: 1 },
    { key: "Note", value: 1 },
    { key: "code", value: 1 },
    { key: "converting", value: 1 },
    { key: "text", value: 1 },
    { key: "rendering", value: 1 },
    { key: "final", value: 1 },
    { key: "output", value: 1 },
    { key: "requires", value: 1 },
    { key: "additional", value: 1 },
    { key: "development", value: 1 },
    { key: "quite", value: 1 },
    { key: "slow", value: 1 },
    { key: "hundred", value: 1 },
    { key: "run", value: 1 },
    { key: "asynchronously", value: 1 },
    { key: "configurable", value: 1 },
    { key: "size", value: 1 },
    { key: "makes", value: 1 },
    { key: "animate", value: 1 },
    { key: "stuttering", value: 1 },
    { key: "recommended", value: 1 },
    { key: "always", value: 1 },
    { key: "use", value: 1 },
    { key: "animations", value: 1 },
    { key: "prevents", value: 1 },
    { key: "browsers", value: 1 },
    { key: "event", value: 1 },
    { key: "loop", value: 1 },
    { key: "blocking", value: 1 },
    { key: "placing", value: 1 },
    { key: "incredibly", value: 1 },
    { key: "important", value: 1 },
    { key: "Attempt", value: 1 },
    { key: "place", value: 1 },
    { key: "point", value: 1 },
    { key: "usually", value: 1 },
    { key: "near", value: 1 },
    { key: "middle", value: 1 },
    { key: "somewhere", value: 1 },
    { key: "central", value: 1 },
    { key: "horizontal", value: 1 },
    { key: "line", value: 1 },
    { key: "intersects", value: 1 },
    { key: "one", value: 1 },
    { key: "along", value: 1 },
    { key: "increasing", value: 1 },
    { key: "spiral", value: 1 },
    { key: "Repeat", value: 1 },
    { key: "intersections", value: 1 },
    { key: "found", value: 1 },
    { key: "hard", value: 1 },
    { key: "part", value: 1 },
    { key: "making", value: 1 },
    { key: "efficiently", value: 1 },
    { key: "According", value: 1 },
    { key: "Jonathan", value: 1 },
    { key: "Feinberg", value: 1 },
    { key: "Wordle", value: 1 },
    { key: "uses", value: 1 },
    { key: "combination", value: 1 },
    { key: "boxes", value: 1 },
    { key: "quadtrees", value: 1 },
    { key: "achieve", value: 1 },
    { key: "reasonable", value: 1 },
    { key: "speeds", value: 1 },
    { key: "Glyphs", value: 1 },
    { key: "JavaScript", value: 1 },
    { key: "isnt", value: 1 },
    { key: "way", value: 1 },
    { key: "precise", value: 1 },
    { key: "glyph", value: 1 },
    { key: "shapes", value: 1 },
    { key: "via", value: 1 },
    { key: "DOM", value: 1 },
    { key: "except", value: 1 },
    { key: "perhaps", value: 1 },
    { key: "SVG", value: 1 },
    { key: "fonts", value: 1 },
    { key: "Instead", value: 1 },
    { key: "hidden", value: 1 },
    { key: "canvas", value: 1 },
    { key: "element", value: 1 },
    { key: "Retrieving", value: 1 },
    { key: "many", value: 1 },
    { key: "batch", value: 1 },
    { key: "Sprites", value: 1 },
    { key: "initial", value: 1 },
    { key: "performed", value: 1 },
    { key: "using", value: 1 },
    { key: "doesnt", value: 1 },
    { key: "copy", value: 1 },
    { key: "appropriate", value: 1 },
    { key: "position", value: 1 },
    { key: "representing", value: 1 },
    { key: "advantage", value: 1 },
    { key: "involves", value: 1 },
    { key: "relevant", value: 1 },
    { key: "rather", value: 1 },
    { key: "previous", value: 1 },
    { key: "Somewhat", value: 1 },
    { key: "surprisingly", value: 1 },
    { key: "lowlevel", value: 1 },
    { key: "hack", value: 1 },
    { key: "made", value: 1 },
    { key: "tremendous", value: 1 },
    { key: "difference", value: 1 },
    { key: "constructing", value: 1 },
    { key: "compressed", value: 1 },
    { key: "blocks", value: 1 },
    { key: "1bit", value: 1 },
    { key: "32bit", value: 1 },
    { key: "integers", value: 1 },
    { key: "thus", value: 1 },
    { key: "reducing", value: 1 },
    { key: "number", value: 1 },
    { key: "checks", value: 1 },
    { key: "memory", value: 1 },
    { key: "times", value: 1 },
    { key: "fact", value: 1 },
    { key: "turned", value: 1 },
    { key: "beat", value: 1 },
    { key: "quadtree", value: 1 },
    { key: "everything", value: 1 },
    { key: "tried", value: 1 },
    { key: "areas", value: 1 },
    { key: "font", value: 1 },
    { key: "sizes", value: 1 },
    { key: "primarily", value: 1 },
    { key: "needs", value: 1 },
    { key: "test", value: 1 },
    { key: "per", value: 1 },
    { key: "whereas", value: 1 },
    { key: "compare", value: 1 },
    { key: "every", value: 1 },
    { key: "overlaps", value: 1 },
    { key: "slightly", value: 1 },
    { key: "Another", value: 1 },
    { key: "possibility", value: 1 },
    { key: "merge", value: 1 },
    { key: "fairly", value: 1 },
    { key: "though", value: 1 },
    { key: "compared", value: 1 },
    { key: "analagous", value: 1 },
    { key: "mask", value: 1 },
    { key: "essentially", value: 1 },
    { key: "ORing", value: 1 },
    { key: "block", value: 1 }
  ];
  
  const chart = new Chart(document.getElementById("canvas").getContext("2d"), {
    type: "wordCloud",
    data: {
      labels: words.map((d) => d.key),
      datasets: [
        {
          label: "",
          data: words.map((d) => 10 + d.value * 10)
        }
      ]
    },
    options: {
      title: {
        display: false,
        text: "Chart.js Word Cloud"
      },
      plugins: {
        legend: {
          display: false
        }
      }
    }
  });


  function word_graph(user_data, spotify_data){


    var wordgraph = document.getElementById('wordgraph').getContext('2d');

    new Chart(wordgraph, {
        type: "wordCloud",
        data: {
          labels: user_data,
          datasets: [
            {
              label: "",
              data: spotify_data
            }
          ]
        },
        options: {
          title: {
            display: false,
            text: "Chart.js Word Cloud"
          },
          plugins: {
            legend: {
              display: false
            }
          }
        }
      });
}
  