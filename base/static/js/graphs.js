
// const vehicleUsageData = JSON.parse('{{ vehicle_usage_data|escapejs }}');
// const driverEarningsData = JSON.parse('{{ driver_earnings_data|escapejs }}');

// // Vehicle Usage Chart
// const vehicleUsageChart = new Chart(document.getElementById("vehicleUsageChart").getContext("2d"), {
//   type: "bar",
//   data: {
//     labels: vehicleUsageData.vehicles,
//     datasets: [
//       {
//         label: "Total Trips",
//         data: vehicleUsageData.total_trips,
//         backgroundColor: "rgba(255, 159, 64, 0.2)",
//         borderColor: "rgba(255, 159, 64, 1)",
//         borderWidth: 1,
//       },
//       {
//         label: "Total Distance",
//         data: vehicleUsageData.total_distance,
//         backgroundColor: "rgba(54, 162, 235, 0.2)",
//         borderColor: "rgba(54, 162, 235, 1)",
//         borderWidth: 1,
//       },
//     ],
//   },
//   options: {
//     scales: {
//       y: {
//         beginAtZero: true,
//       },
//     },
//   },
// });

// // Driver Earnings Chart
// const driverEarningsChart = new Chart(document.getElementById("driverEarningsChart").getContext("2d"), {
//   type: "bar",
//   data: {
//     labels: driverEarningsData.drivers,
//     datasets: [
//       {
//         label: "Total Earnings",
//         data: driverEarningsData.total_earnings,
//         backgroundColor: "rgba(255, 99, 132, 0.2)",
//         borderColor: "rgba(255, 99, 132, 1)",
//         borderWidth: 1,
//       },
//       {
//         label: "Total Trips",
//         data: driverEarningsData.total_trips,
//         backgroundColor: "rgba(255, 205, 86, 0.2)",
//         borderColor: "rgba(255, 205, 86, 1)",
//         borderWidth: 1,
//       },
//     ],
//   },
//   options: {
//     scales: {
//       y: {
//         beginAtZero: true,
//       },
//     },
//   },
// });
