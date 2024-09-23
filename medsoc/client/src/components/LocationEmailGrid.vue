<template>
  <div v-if="locationEmailData" class="container mt-4">
    <h4>Assignments</h4>
    <div v-if="!isEmpty(locationEmailData)" class="row">
      <!-- Loop through the dictionary passed as prop -->
      <div class="col-md-4" v-for="(emails, location) in locationEmailData" :key="location">
        <div class="card mb-4">
          <div class="card-header">
            <h5 class="card-title">{{ location }}</h5>
          </div>
          <div class="card-body">
            <ul class="list-group list-group-flush">
              <li 
                class="list-group-item" 
                v-for="(email, index) in emails" 
                :key="email" 
                :class="{ active: index === 0, 'small-text': true }"
              >
                {{ email }}
              </li>
            </ul>
          </div>
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
      default: () => ({}),
    },
  },
  methods: {
    isEmpty(obj) {
      return Object.keys(obj).length === 0;
    },
  },
};
</script>

<style scoped>
.card-header {
  background-color: #f8f9fa;
}

.small-text {
  font-size: 0.9rem;
}
</style>
