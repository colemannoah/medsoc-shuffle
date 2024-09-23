<template>
  <div class="container mt-4">
    <h4>Leftover People ({{ leftovers.length }})</h4>
    <table v-if="leftovers.length > 0" class="table table-striped">
      <thead>
        <tr>
          <th>Email</th>
          <th>Year Group</th>
          <th>Preferences</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(person, index) in leftovers" :key="index">
          <td>{{ person.email }}</td>
          <td>{{ person.year }}</td>
          <td>{{ person.preferences.join(', ') }}</td>
        </tr>
      </tbody>
    </table>
    <div v-else class="container mt-4">
      <p>No data to display</p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    leftovers: {
      type: Array,
      required: true,
    },
  },
};
</script>
