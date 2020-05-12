$.getJSON(
    "/token",
    {
      device: "browser"
    },
    function(data) {
      // Alert the user they have been assigned a random username
      username = data.identity;
      print(
        "You have been assigned a random username of: " +
          '<span class="me">' +
          username +
          "</span>",
        true
      );
 
      // Initialize the Chat client
      Twilio.Chat.Client.create(data.token).then(client => {
        // Use client
        chatClient = client;
        chatClient.getSubscribedChannels().then(createOrJoinChannel);
      });
    }
  );

function createOrJoinChannel() {
  // Extract the room's channel name from the page URL
  let channelName = window.location.pathname.split("/").slice(-2, -1)[0];

  print(`Attempting to join the "${channelName}" chat channel...`);

  chatClient
    .getChannelByUniqueName(channelName)
    .then(function(channel) {
      roomChannel = channel;
      setupChannel(channelName);
    })
    .catch(function() {
      // If it doesn't exist, let's create it
      chatClient
        .createChannel({
          uniqueName: channelName,
          friendlyName: `${channelName} Chat Channel`
        })
        .then(function(channel) {
          roomChannel = channel;
          setupChannel(channelName);
        });
    });
}

function setupChannel(name) {
  roomChannel.join().then(function(channel) {
    print(
      `Joined channel ${name} as <span class="me"> ${username} </span>.`,
      true
    );
    channel.getMessages(30).then(processPage);
  });

  // Listen for new messages sent to the channel
  roomChannel.on("messageAdded", function(message) {
    printMessage(message.author, message.body);
  });
}
function processPage(page) {
  page.items.forEach(message => {
    printMessage(message.author, message.body);
  });
  if (page.hasNextPage) {
    page.nextPage().then(processPage);
  } else {
    console.log("Done loading messages");
  }
}

let $form = $("#message-form");
let $input = $("#message-input");
$form.on("submit", function(e) {
  e.preventDefault();
  if (roomChannel && $input.val().trim().length > 0) {
    roomChannel.sendMessage($input.val());
    $input.val("");
  }
});