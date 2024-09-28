<template>
  <div class="container mt-4">
    <h4>Assignments</h4>
    <div v-if="!isEmpty(locationEmailData)">
      <div v-for="(members, location) in locationEmailData" :key="location" class="card mb-4">
        <div class="card-body">
          <h5 class="card-title mb-2">{{ location }} ({{ members.length }})</h5>
          <table class="table table-striped">
            <thead>
              <tr>
                <th>Email</th>
                <th>Year Group</th>
                <th>Preferences</th>
                <th>Leader Status</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="(member, index) in sortedMembers(members)"
                :key="index"
                :class="{ 'table-primary': member.leader }"
              >
                <td>{{ member.email }}</td>
                <td>{{ member.year }}</td>
                <td>{{ member.preferences.sort().join(', ') }}</td>
                <td>{{ member.leader ? 'Leader' : '' }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <div v-else class="container mt-4">
      <p>No data to display</p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    locationEmailData: {
      type: Object,
      required: true,
      default: () => ({})
    }
  },
  methods: {
    isEmpty(obj) {
      return Object.keys(obj).length === 0
    },
    sortedMembers(members) {
      return [...members].sort((a, b) => b.leader - a.leader)
    }
  }
}
</script>

<style scoped>
.card-header {
  background-color: #f8f9fa;
}

.small-text {
  font-size: 0.9rem;
}
</style>
