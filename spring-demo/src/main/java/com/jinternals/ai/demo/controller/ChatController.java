package com.jinternals.ai.demo.controller;

import com.jinternals.ai.demo.controller.request.ChatRequest;
import com.jinternals.ai.demo.controller.request.EmbedRequest;
import com.jinternals.ai.demo.controller.response.ChatResponse;
import com.jinternals.ai.demo.controller.response.EmbedResponse;
import com.jinternals.ai.demo.services.ChatService;
import lombok.AllArgsConstructor;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/chat")
@Validated
@AllArgsConstructor
public class ChatController {
    private final ChatService service;
    @PostMapping
    public ChatResponse embed(@RequestBody ChatRequest body) {
        var answer = service.coverse(body.question());
        return new ChatResponse(answer);
    }

}
