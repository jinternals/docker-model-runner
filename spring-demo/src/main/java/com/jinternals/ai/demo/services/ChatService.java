package com.jinternals.ai.demo.services;

import lombok.AllArgsConstructor;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.stereotype.Service;


@Service
@AllArgsConstructor
public class ChatService {

    private final ChatClient chatClient;

    public String coverse(String text) {
        return chatClient.prompt(text).call().content();
    }
}
