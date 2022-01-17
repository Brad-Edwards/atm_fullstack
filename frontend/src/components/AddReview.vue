<template>
  <div class="submit-form">
    <div v-if="!submitted">
      <div class="form-group">
        <label for="title">Title</label>
        <input
          type="text"
          class="form-control"
          id="title"
          required
          v-model="review.title"
          name="title"
        />
      </div>

    <div class="form-group">
    <label for="release_year">Release Year</label>
    <input
        type="text"
        class="form-control"
        id="release_year"
        required
        v-model="review.release_year"
        name="release_year"
    />
    </div>
   
    <div class="form-group">
      <label for="duration">Duration</label>
      <input
          type="text"
          class="form-control"
          id="duration"
          required
          v-model="review.duration"
          name="duration"
      />
      </div>
      
      <div class="form-group">
        <label for="description">Description</label>
        <input
            class="form-control"
            id="description"
            required
            v-model="review.description"
            name="description"
        />
        </div> 

      <div class="form-group">
        <label for="poster_uri">Poster URL</label>
        <input
            class="form-control"
            id="poster_uri"
            required
            v-model="review.description"
            name="poster_uri"
        />
        </div>

      <button @click="saveReview" class="btn btn-success">Submit</button>
    </div>

    <div v-else>
      <h4>You submitted successfully!</h4>
      <button class="btn btn-success" @click="newReview">Add</button>
    </div>
  </div>
</template>

<script>
import ReviewDataService from "../services/ReviewDataService";

export default {
  name: "add-review",
  data() {
    return {
      review: {
        id: null,
        title: "",
        description: "",
        release_year: "",
        duration: "",
        poster_uri: "",
      },
      submitted: false
    };
  },
  methods: {
    saveReview() {
      var data = {
        title: this.review.title,
        description: this.review.description,
        release_year: this.review.release_year,
        duration: this.review.duration,
        poster_uri: this.review.poster_uri,
      };

      ReviewDataService.create(data)
        .then(response => {
          this.review.id = response.data.id;
          console.log(response.data);
          this.submitted = true;
        })
        .catch(e => {
          console.log(e);
        });
    },
    
    newReview() {
      this.submitted = false;
      this.review = {};
    }
  }
};
</script>

<style>
.submit-form {
  max-width: 300px;
  margin: auto;
}
</style>