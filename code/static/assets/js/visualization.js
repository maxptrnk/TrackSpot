

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
                '#ffba18',
                '#ff6969',
                '#92caa7',
                '#8d4700',
                '#466c93',
              ],
              
              borderColor: [
                  '#ffba18',
                '#ff6969',
                '#92caa7',
                '#8d4700',
                '#466c93',
              ],

          hoverOffset: 4
          }]},


          options: {
              responsive: true,
              plugins: {
                legend: {
                  position: 'top',
                  labels:{
                      color:'white',
                      font: {size : 16}
                  }
                },
                
              }
            },

          
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
      
          responsive: true,
         
         
              plugins: {
                  legend: {
                      display: true,
                      labels: {
                          color:'white',
                          font: {size : 16}
                      }
                  }
              },
          
         
          
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

          options: {
              responsive: true,
              plugins: {
                legend: {
                  labels:{
                      color:'white',
                      font: {size : 16}
                  }
                },
                
              }
            },


      });
}


//     cols = ['Danceability', 'Energy', 'Acousticness', 'Speechiness', 'Valence', 'Instrumentalness']



