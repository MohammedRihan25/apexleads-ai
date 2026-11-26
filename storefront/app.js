/**
 * ApexLeads AI — B2B Storefront & Intake Controller
 */

let selectedPlan = "Growth Engine";
let selectedPrice = 397;

function openOrderModal(planName, price) {
  selectedPlan = planName;
  selectedPrice = price;
  
  const titleElem = document.getElementById("modalPlanTitle");
  if (titleElem) {
    titleElem.innerText = `Configure ${planName} ($${price})`;
  }
  
  const modal = document.getElementById("orderModal");
  if (modal) {
    modal.style.display = "flex";
  }
}

function closeOrderModal() {
  const modal = document.getElementById("orderModal");
  if (modal) {
    modal.style.display = "none";
  }
}

// Close modal when clicking outside of the card
window.addEventListener("click", function(event) {
  const modal = document.getElementById("orderModal");
  if (event.target === modal) {
    closeOrderModal();
  }
});

function handleOrderSubmit(e) {
  e.preventDefault();
  
  const email = document.getElementById("clientEmail").value;
  const niche = document.getElementById("targetNiche").value;
  const location = document.getElementById("targetLocation").value;
  const titles = document.getElementById("targetTitles").value;
  const payment = document.getElementById("paymentMethod").value;
  
  const orderPayload = {
    plan: selectedPlan,
    price_usd: selectedPrice,
    client_email: email,
    target_niche: niche,
    target_location: location,
    target_titles: titles,
    payment_method: payment,
    timestamp: new Date().toISOString()
  };
  
  // Store order locally
  const previousOrders = JSON.parse(localStorage.getItem("apexleads_orders") || "[]");
  previousOrders.push(orderPayload);
  localStorage.setItem("apexleads_orders", JSON.stringify(previousOrders));
  
  closeOrderModal();
  
  // Show confirmation notice
  const notice = document.getElementById("successNotice");
  if (notice) {
    notice.style.display = "block";
    notice.innerHTML = `<strong>Order Intake Recorded for ${email}!</strong><br>We have queued harvesting for <em>${niche} (${location})</em>. Our team is generating your invoice.`;
    setTimeout(() => {
      notice.style.display = "none";
    }, 6000);
  }
  
  // Reset form
  document.getElementById("orderForm").reset();
}
