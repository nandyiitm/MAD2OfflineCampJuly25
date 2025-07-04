<template>
    <h2>Admin dashboard</h2>

    <form @submit.prevent="handleSubmit">
        <label for="author_name">Author Name</label>
        <input v-model="name" type="text" id="author_name" required>
        <label for="author_image">Author Image Link</label>
        <input v-model="link" type="text" id="author_image" required>
        <label for="quote_text">Quote Text</label>
        <textarea v-model="text" name="" id="quote_text" required></textarea>

        <button>Create Quote</button>
    </form>

    <h2>Quotes</h2>
    <div v-if="quotes.length">
        <li v-for="quote in quotes">
            {{ quote.author }} - {{ quote.text }}
            <img :src="quote.author_image" alt="">


            <button @click="deletQuote(quote.id)" style="color: red;">Delete</button>
        </li>
    </div>
    <div v-else>
        No quotes available
    </div>

</template>

<script>
export default {
    name: 'AdminDashboard',
    data() {
        return {
            name: 'abdulkalam',
            link: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSl9YTF4GEH91Kf5Ujafe3yVceweglr6MrNDw&s',
            text: 'If you want to shine like a sun, first burn like a sun',
            quotes: []
        }
    },
    methods: {
        handleSubmit() {
            const formData = {
                'author': this.name, 'author_image': this.link, 'text': this.text
            }
            const jwtToken = localStorage.getItem('token')
          fetch('http://127.0.0.1:5000/quotes', {
              method: 'POST', // Specify the HTTP method
              headers: {
                'Content-Type': 'application/json', // Indicate JSON content
                'Authorization': `Bearer ${jwtToken}`
              },
              body: JSON.stringify(formData) // Convert JavaScript object to JSON string
            })
            .then(response => {
                if (!response.ok) {
                    if (response.status === 401) {
                        alert("You are not allowed to perform this action")
                        this.$router.push('/user')
                    }
                    alert(response.status)
                }
                console.log(response.status)
                return response.json()
            })
            .then(data => {
                console.log('Response from POST', data)
                window.location.reload()
            })
            .catch( error => {
                console.log(error)
            })
        },
        getQuotes() {
            const jwtToken = localStorage.getItem('token')
          fetch('http://127.0.0.1:5000/quotes', {
              method: 'GET', // Specify the HTTP method
              headers: {
                'Content-Type': 'application/json', // Indicate JSON content
                'Authorization': `Bearer ${jwtToken}`
              },
            })
            .then(response => {
                if (!response.ok) {
                    if (response.status === 401) {
                        alert("You are not allowed to perform this action")
                        this.$router.push('/user')
                    }
                    alert(response.status)
                }
                console.log(response.status)
                return response.json()
            })
            .then(data => {
                console.log('Response from POST', data)
                this.quotes = data.quotes
            })
            .catch( error => {
                console.log(error)
            })
        },
        deletQuote(id) {
            // alert(`deleting quote - ${id}`)
            const jwtToken = localStorage.getItem('token')
            fetch(`http://127.0.0.1:5000/quotes/${id}`, {
                method: 'DELETE', // Specify the HTTP method
                headers: {
                    'Content-Type': 'application/json', // Indicate JSON content
                    'Authorization': `Bearer ${jwtToken}`
                },
                })
            window.location.reload()
        }
    },
    mounted() {
        this.getQuotes()
    }
}
</script>