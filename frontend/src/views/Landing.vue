<script setup>
import Topbar from '../components/Topbar.vue'
function smoothScroll(id) {
    document.body.click();
    document.querySelector(id).scrollIntoView({
        behavior: 'smooth'
    });
}
</script>

<template>
<div >
    <Topbar />
</div>


</template>

<script>


</script>

<style>
.table__body {
  width: 100%;
  background-color: #fffb;
  margin: .8rem auto;
  border-radius: .6rem;
  overflow-x: auto; /* Enable horizontal scrolling */
}

.table__body::-webkit-scrollbar {
  height: 0.5rem; /* Horizontal scrollbar height */
}

.table__body::-webkit-scrollbar-thumb {
  border-radius: .5rem;
  background-color: #0004;
  visibility: hidden;
}

.table__body:hover::-webkit-scrollbar-thumb {
  visibility: visible;
}

table {
  width: 100%;
  table-layout: fixed; /* Maintain fixed table layout */
}

table, th, td {
  border-collapse: collapse;
  padding: 1rem;
  text-align: left;
}

thead th {
  position: sticky;
  top: 0;
  left: 0;
  background-color: #d5d1defe;
  cursor: pointer;
  text-transform: capitalize;
}

tbody tr:nth-child(even) {
  background-color: #0000000b;
}

tbody tr {
  --delay: .1s;
  transition: .5s ease-in-out var(--delay), background-color 0s;
}

tbody tr:hover {
  background-color: #fff6 !important;
}

tbody tr td,
tbody tr td p,
tbody tr td img {
  transition: .2s ease-in-out;
}

tbody tr.hide td,
tbody tr.hide td p {
  padding: 0;
  font: 0 / 0 sans-serif;
  transition: .2s ease-in-out .5s;
}

tbody tr.hide td img {
  width: 0;
  height: 0;
  transition: .2s ease-in-out .5s;
}

.status {
  padding: .4rem 0;
  border-radius: 2rem;
  text-align: center;
}

.status.delivered {
  background-color: #86e49d;
  color: #006b21;
}

.status.cancelled {
  background-color: #d893a3;
  color: #b30021;
}

.status.pending {
  background-color: #ebc474;
}

.status.shipped {
  background-color: #6fcaea;
}

/* Media query for screen sizes 620px or less */
@media (max-width: 620px) {
  .dashboard {
    margin: 0 5%;
    padding: 5px;
    width: 90%;
  }

  .table__body {
    margin: 0;
  }

  table {
    table-layout: auto; /* Allow table to adjust layout based on content */
  }

  thead th,
  tbody td {
    padding: 0.5rem; /* Adjust padding for smaller screens */
    font-size: 0.9rem; /* Adjust font size for better fit */
  }
}
</style>