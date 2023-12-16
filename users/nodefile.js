const arr = [
  {
    "id": 119,
    "date": "2023-11-22",
    "is_present": false,
    "student": "a3116117-7162-4acb-9ac4-1b81fbcf0307",
    "class_attended": "de09f2a2-97f2-4dc2-a170-70302f95f509"
  },
  {
    "id": 316,
    "date": "2023-08-01",
    "is_present": false,
    "student": "a3116117-7162-4acb-9ac4-1b81fbcf0307",
    "class_attended": "049943eb-63ee-412d-ac87-c97677b84be3"
  },
  {
    "id": 513,
    "date": "2023-05-25",
    "is_present": true,
    "student": "a3116117-7162-4acb-9ac4-1b81fbcf0307",
    "class_attended": "6f67ec02-d5dc-4ed7-99ff-62aa0e3e2116"
  },
  {
    "id": 710,
    "date": "2023-02-09",
    "is_present": true,
    "student": "a3116117-7162-4acb-9ac4-1b81fbcf0307",
    "class_attended": "049943eb-63ee-412d-ac87-c97677b84be3"
  },
  {
    "id": 907,
    "date": "2023-04-30",
    "is_present": false,
    "student": "a3116117-7162-4acb-9ac4-1b81fbcf0307",
    "class_attended": "c7241506-b4d0-454e-8cf8-b6302a9ea2a7"
  }
];
const attendanceFunc = (attendances) => {
  let numPresent = 0, numAbsent = 0;
  attendances.map((item) => {
    numPresent = item.is_present ? numPresent + 1 : numPresent
    numAbsent = item.is_present ? numAbsent : numAbsent + 1
    // console.log(numPresent, numAbsent);
  });
  return [numPresent, numAbsent]
}
// console.log(arr);
let [numPresent, numAbsent] = attendanceFunc();
console.log(numPresent, numAbsent);