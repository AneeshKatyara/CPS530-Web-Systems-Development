function showBookmarks() {
const links = [
"https://www.google.com",
"https://www.torontomu.ca",
"http://neverssl.com"
];
const secureIcon = "🔒";
const insecureIcon = "
🔓
";
const container = document.getElementById("bookmarks");
const list = document.createElement("ul");
links.forEach(url => {
const li = document.createElement("li");
const icon = url.startsWith("https") ? secureIcon : insecureIcon;
const iconClass = url.startsWith("https") ? "secure" : "insecure";
li.innerHTML = `<span class="${iconClass}">${icon}</span>
<a href="${url}" target="_blank">${url}</a>`;
list.appendChild(li);
});
container.appendChild(list);
}
/*
Problem 2 - Palindrome Checker
*/
function cleanString(str) {
return str
.toLowerCase()
.replace(/[^a-z0-9]/g,
"");
}
function isPalindrome(str) {
const cleaned = cleanString(str);
const reversed = cleaned.split("").reverse().join("");
return cleaned === reversed;
}
function showPalindromes() {
const testStrings = [
"Mr. Owl ate my metal worm.",
"I’m on a seafood diet. I see food and I eat it.",
"level",
"Love is sharing your popcorn.",
"Was it a car or a cat I saw?",
"madam",
"JavaScript is fun"
];
const container = document.getElementById("palindromes");
testStrings.forEach(str => {
const result = document.createElement("p");
if (isPalindrome(str)) {
result.className = "palindrome";
result.innerHTML = `<strong>${str}</strong> → ✅ Palindrome`;
} else {
result.className = "not-palindrome";
result.innerHTML = `<strong>${str}</strong> → ❌ Not a palindrome`;
}
container.appendChild(result);
});
}
document.addEventListener("DOMContentLoaded", () => {
showBookmarks();
showPalindromes();
});
